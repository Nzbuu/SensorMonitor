import sys
from SensorMonitor.monitor import Monitor

__author__ = 'James Myatt'


def main():
    """Main entry point for the script."""
    m = Monitor()
    try:
        m.run()
    except KeyboardInterrupt:
        print("Goodbye!")
    finally:
        print("Stop!")


if __name__ == '__main__':
    sys.exit(main())
