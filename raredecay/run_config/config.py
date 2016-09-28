# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:44:43 2016

The configuration file for external operations.

@author: mayou
"""



from raredecay import meta_config



RUN_NAME = 'Classifier optimization'
run_message = str("This could be your advertisement" +
                " ")



OUTPUT_CFG = dict(
    run_name=RUN_NAME,
    output_path='/home/mayou/Documents/uniphysik/Bachelor_thesis/output/',
    del_existing_folders=False,
    output_folders=dict(
        log="log",
        plots="plots",
        results="results",
        config="config"
    )
)


#==============================================================================
# LOGGER CONFIGURATION BEGIN
#==============================================================================
logger_cfg = dict(
    logging_mode='both',   # define where the logger is written to
    # take 'both', 'file', 'console' or 'no'
    log_level_file='debug',
    # specifies the level to be logged to the file
    log_level_console='debug', #'warning',
    # specify the level to be logged to the console
    overwrite_file=True,
    # specifies whether it should overwrite the log file each time
    # or instead make a new one each run
    log_file_name='logfile_',
    # the beginning ofthe name of the logfile, like 'project1'
    log_file_dir=None  # will be set automatically
)