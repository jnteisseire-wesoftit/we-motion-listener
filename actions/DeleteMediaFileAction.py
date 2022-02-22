import os
import logging.handlers

logger = logging.getLogger('MotionNotify')

class DeleteMediaFileAction:
    @staticmethod
    def do_event_start_action(config, motion_event):
        logger.info("Motionevent_id:" + motion_event.event_id.__str__() + " Deleting: %s", motion_event.media_file)
        DeleteMediaFileAction.delete_file(motion_event.media_file)

    @staticmethod
    def do_event_end_action(config, motion_event):
        logger.info("Motionevent_id:" + motion_event.event_id.__str__() + " Deleting: %s", motion_event.media_file)
        DeleteMediaFileAction.delete_file(motion_event.media_file)

    @staticmethod
    def do_action(config, motion_event):
        logger.info("Motionevent_id:" + motion_event.event_id.__str__() + " Deleting: %s", motion_event.media_file)
        DeleteMediaFileAction.delete_file(motion_event.media_file)

    @staticmethod
    def delete_file(file_path):
        os.remove(file_path)