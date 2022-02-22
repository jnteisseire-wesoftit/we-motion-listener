import os.path
import sys
import logging.handlers
import traceback
from objects import motion_event as motion_event_mod
from utils import utils as utils_mod

logger = logging.getLogger('WeMotionListener')

hdlr = logging.handlers.RotatingFileHandler('/var/log/we-motion-listener/we-motion-listener.log',
                                            maxBytes=1048576,
                                            backupCount=3)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)


def loggerExceptHook(t, v, tb):
    logger.error(traceback.format_exception(t, v, tb))


class MotionListener:
    def handle_event(self):
        logger.debug("Handling Event Actions...")

        actions_for_event = self.motion_event_obj.get_actions_for_event(self.config_obj, self.is_system_active)
        for action in actions_for_event:
            logger.info(
                "Handling action: " + action + " for event ID " + self.motion_event_obj.event_id + " with event_type " + self.motion_event_obj.event_type.__str__())
            klass = utils_mod.Utils.reflect_class_from_classname('actions', action)
            if self.motion_event_obj.event_type == event_type_mod.EventType.on_event_start:
                klass.do_event_start_action(self.config_obj, motion_event_obj)
            elif self.motion_event_obj.event_type == event_type_mod.EventType.on_picture_save or self.motion_event_obj.event_type == event_type_mod.EventType.on_cron_trigger:
                klass.do_action(self.config_obj, motion_event_obj)
            elif self.motion_event_obj.event_type == event_type_mod.EventType.on_movie_end:
                klass.do_event_end_action(self.config_obj, motion_event_obj)
        logger.debug("All events actions handled...")

    def __init__(self, config_obj, motion_event_obj):
        logger.debug("Initializing...")
        self.config_obj = config_obj
        self.motion_event_obj = motion_event_obj
        self.is_system_active = False
        self.handle_event()


if __name__ == '__main__':
    logger.info("Motion Listener script started")
    try:

        if len(sys.argv) < 6:
            exit(
                'Motion Listener - Usage: we-motion-listener.py {config-file-path} {media-file-path} {event-type on_event_start, on_picture_save, on_movie_end or on_cron_trigger} {timestamp} {event_id} {file_type} ')

        cfg_path = sys.argv[1]
        if not os.path.exists(cfg_path):
            exit('Config file does not exist [%s]' % cfg_path)

        motion_event_obj = motion_event_mod.MotionEvent(sys.argv[2], event_type_mod.EventType[sys.argv[3]], sys.argv[4],
                                                        sys.argv[5],
                                                sys.argv[6])

        MotionListener(config_mod.Config(cfg_path), motion_event_obj)
    except Exception as e:
        logger.error("Initialization error..." + e.__str__())
        exit('Error: [%s]' % e)