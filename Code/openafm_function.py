    #continued after V1



def gwybas(filename):
    #add the gwyddion folders to the path, making sure they can be found
    import sys
    sys.path.append('C:\Program Files (x86)\Gwyddion\\bin')
    sys.path.append('C:\Program Files (x86)\Gwyddion\share\gwyddion\pygwy')

    #import gwyddion
    import gwy
    import gwyutils

    #load the file and add to data browser
    c = gwy.gwy_file_load(filename, gwy.RUN_IMMEDIATE)
    gwy.gwy_app_data_browser_add(c)


    #Set the right settings for the align_rows command
    settings = gwy.gwy_app_settings_get()

    settings['/module/linematch/direction'] = int(gwy.ORIENTATION_HORIZONTAL)
    settings['/module/linematch/do_extract'] = False
    settings['/module/linematch/do_plot'] = False
    settings['/module/linematch/method'] = 0   # 0: poly, 1: median, 2: median of diff,3: modus,4: matching, 5: trimemd mean, 6: trimmed mean of diff
    settings['/module/linematch/masking'] = 2
    settings['/module/linematch/max_degree'] = 3    #Order of polynominal
    settings['/module/linematch/trim_fraction'] = 0.05

    #print the datafield ID's corresponding to the different channels of the AFM, such as height, phase and error, usually the first one (0) is the height
    # print gwy.gwy_app_data_browser_get_data_ids(c)

    #itterate over the different datafield ID's/AFM channels, and do processing on them
    for datafield_id in gwy.gwy_app_data_browser_get_data_ids(c):
        # datafield = c['/%d/data' % datafield_id]

        #set the color range to automatic with tials cut off (corresponding to number 2)
        c['/%d/base/range-type' % datafield_id] = 2

        #select the datafield_ID/AFM channel to process
        gwy.gwy_app_data_browser_select_data_field(c, datafield_id)

        #level the plane
        gwy.gwy_process_func_run("level", c, gwy.RUN_IMMEDIATE)

        #align the rows, with settings chosen above line 19-25
        gwy.gwy_process_func_run("align_rows", c, gwy.RUN_IMMEDIATE)

        #remove scars a couple of times (button bashing)
        gwy.gwy_process_func_run("scars_remove", c, gwy.RUN_IMMEDIATE)
        gwy.gwy_process_func_run("scars_remove", c, gwy.RUN_IMMEDIATE)
        gwy.gwy_process_func_run("scars_remove", c, gwy.RUN_IMMEDIATE)
        gwy.gwy_process_func_run("scars_remove", c, gwy.RUN_IMMEDIATE)
        gwy.gwy_process_func_run("scars_remove", c, gwy.RUN_IMMEDIATE)

        #fix lowest point to zero
        gwy.gwy_process_func_run('fix_zero', c, gwy.RUN_IMMEDIATE)

    #define new file names, I chose to simply add the wanted extention to the original filename
    newname=filename+'.gwy'
    newname2=filename+'.jpg'

    #find the ID/Channel corresponding to the height, of this one a JPG will be created, .gwy will contain all channels
    ids = gwy.gwy_app_data_browser_find_data_by_title(c, 'Height')
    gwy.gwy_app_data_browser_select_data_field(c, ids[0])
    gwy.gwy_file_save(c, newname, gwy.RUN_NONINTERACTIVE)
    gwy.gwy_file_save(c, newname2, gwy.RUN_NONINTERACTIVE)

    #remove the current container, makes room for the next file
    gwy.gwy_app_data_browser_remove(c)