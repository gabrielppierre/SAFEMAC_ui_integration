def connect_buttons(widgets, camera_manager, open_image_selection_dialog):
    # Conectando botões aos métodos correspondentes
    widgets.btn_visualize.clicked.connect(camera_manager.show_cameras_page)
    widgets.hide_configs_camera.clicked.connect(camera_manager.toggle_bottom_configs)
    widgets.btn_visu.clicked.connect(camera_manager.view_recordings)
    widgets.btn_add_camera.clicked.connect(camera_manager.add_camera_clicked)
    widgets.btn_recordings.clicked.connect(camera_manager.add_recordings)
    widgets.btn_init_rec.clicked.connect(camera_manager.start_recording)
    widgets.btn_stop_rec.clicked.connect(camera_manager.stop_recording)
    widgets.btn_stop_visu.clicked.connect(camera_manager.stop_visu)
    widgets.btn_new_video.clicked.connect(open_image_selection_dialog)
