/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * server.c
 * Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
 *
 * full_simple_new is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * full_simple_new is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */
#include "shared_memory.h"

int main(void)
{
    //////////////////////////////////////////////////////////////////////////
    /// Log file for collecting all transcripts
    int fd_log = open(
        SHM_LOGFILE, O_CREAT | O_WRONLY | O_APPEND | O_SYNC, 0666
    );

    if (fd_log == -1)
    {
        perror("Failed to open log file for incoming messages.");
        exit(SHM_ERROR);
    }

    //////////////////////////////////////////////////////////////////////////
    /// Mutual exclusion semaphore shared memory
    sem_t *mutex_sem = sem_open(SHM_SEM_MUTEX_NAME, O_CREAT, 0660, 0);

    if (mutex_sem == SEM_FAILED)
    {
        perror("Failed to open shared memory segment SHM SEM MUTEX.");
        exit(SHM_ERROR);
    }

    //////////////////////////////////////////////////////////////////////////
    /// Gets shared memory
    int fd_shm = shm_open(SHM_NAME, O_RDWR | O_CREAT | O_EXCL, 0660);

    if (fd_shm == -1)
    {
        perror("Failed to open shared memory segment.");
        exit(SHM_ERROR);
    }

    //////////////////////////////////////////////////////////////////////////
    /// 
    if (ftruncate(fd_shm, sizeof(struct shared_memory)) == -1)
    {
        perror("Failed shared memory segment truncate.");
        exit(SHM_ERROR);
    }

    //////////////////////////////////////////////////////////////////////////
    /// Map shared memory to process address space 
    struct shared_memory *shared_mem_ptr = mmap(
        NULL,
        sizeof(struct shared_memory),
        PROT_READ | PROT_WRITE,
        MAP_SHARED,
        fd_shm,
        0
    );

    if (shared_mem_ptr == MAP_FAILED)
    {
        perror("Failed to map shared memory segment.");
        exit(SHM_ERROR);
    }

    //////////////////////////////////////////////////////////////////////////
    /// Initialize the shared memory
    shared_mem_ptr->buffer_index = shared_mem_ptr->buffer_print_index = 0;

    //////////////////////////////////////////////////////////////////////////
    /// Counting semaphore  indicating the number of available buffers
    sem_t *buffer_count_sem = sem_open(
        SHM_SEM_BUFFER_COUNT_NAME, O_CREAT | O_EXCL, 0660, SHM_MAX_BUFFERS
    );

    if (buffer_count_sem == SEM_FAILED)
    {
        perror("Failed to open shared memory segment SHM SEM BUFFER COUNT.");
        exit(SHM_ERROR);
    }

    //////////////////////////////////////////////////////////////////////////
    /// Counting semaphore indicating the number of strings to be printed
    sem_t *spool_signal_sem = sem_open(
        SHM_SEM_SPOOL_SIGNAL_NAME, O_CREAT | O_EXCL, 0660, 0
    );

    if (spool_signal_sem == SEM_FAILED)
    {
        perror("Failed to open shared memory segment SHM SEM SPOOL SIGNAL.");
        exit(SHM_ERROR);
    }

    //////////////////////////////////////////////////////////////////////////
    /// Initialization complete; now we can set mutex semaphore as 1 to
    /// indicate shared memory segment is available
    if (sem_post(mutex_sem) == -1)
    {
        perror("SEM_POST: Failed mutex semaphore.");
        exit(SHM_ERROR);
    }

    //////////////////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////////
    /// Integration section

    char buffer[SHM_SIZE_BUFFER] = {0};

    while (1)
    {
        //////////////////////////////////////////////////////////////////////
        /// Is there a string to print? P (spool_signal_sem);
        if (sem_wait(spool_signal_sem) == -1)
        {
            perror("SEM_WAIT: Failed spool signal semaphore.");
            exit(SHM_ERROR);
        }

        strncpy(
            buffer,
            shared_mem_ptr->buffer[shared_mem_ptr->buffer_print_index],
            SHM_SIZE_BUFFER - 1
        );

        //////////////////////////////////////////////////////////////////////
        /// Since there is only one process (the logger) using the
        /// buffer_print_index, mutex semaphore is not necessary
        (shared_mem_ptr->buffer_print_index)++;

        if (shared_mem_ptr->buffer_print_index == SHM_MAX_BUFFERS)
        {
            shared_mem_ptr->buffer_print_index = 0;
        }

        //////////////////////////////////////////////////////////////////////
        /// Contents of one buffer has been printed.
        /// One more buffer is available for use by producers.
        /// Release buffer: V (buffer_count_sem);
        if (sem_post(buffer_count_sem) == -1)
        {
            perror("SEM_POST: Failed buffer count semaphore.");
            exit(SHM_ERROR);
        }

        //////////////////////////////////////////////////////////////////////
        /// Writes the message to log file
        if ((size_t) write(fd_log, buffer, strlen(buffer)) != strlen(buffer))
        {
            perror("Failed to write message to log file.");
            exit(SHM_ERROR);
        }
    }

    /// Integration section
    //////////////////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////////

    if(munmap(shared_mem_ptr, sizeof(struct shared_memory)) == -1)
    {
        perror("Failed to unmap shared memory segment.");
        close(fd_shm);
        close(fd_log);
        exit(SHM_ERROR);
    }

    if(close(fd_shm) == -1)
    {
        perror("Failed to close shared memory segment.");
        close(fd_log);
        exit(SHM_ERROR);
    }

    if(close(fd_log) == -1)
    {
        perror("Failed to close log file.");
        exit(SHM_ERROR);
    }

    if(sem_close(mutex_sem) == -1)
    {
        perror("Failed to mutex semaphore.");
        exit(SHM_ERROR);
    }

    if(sem_close(buffer_count_sem) == -1)
    {
        perror("Failed to close buffer count semaphore.");
        exit(SHM_ERROR);
    }

    if(sem_close(spool_signal_sem) == -1)
    {
        perror("Failed to close spool signal semaphore.");
        exit(SHM_ERROR);
    }

    if(sem_unlink(SHM_SEM_MUTEX_NAME) == -1)
    {
        perror("Failed to close semaphore mutex.");
        exit(SHM_ERROR);
    }

    if(sem_unlink(SHM_SEM_BUFFER_COUNT_NAME) == -1)
    {
        perror("Failed to unlink semaphore buffer count.");
        exit(SHM_ERROR);
    }

    if(sem_unlink(SHM_SEM_SPOOL_SIGNAL_NAME) == -1)
    {
        perror("Failed to unlink spool signal semaphore.");
        exit(SHM_ERROR);
    }

    if(shm_unlink(SHM_NAME) == -1)
    {
        perror("Failed to unlink shared memory.");
        exit(SHM_ERROR);
    }

    return 0;
}
