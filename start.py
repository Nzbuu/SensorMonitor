import sys
from SensorMonitor.Monitor import Monitor

__author__ = 'James Myatt'


def main():
    """Main entry point for the script."""
    m = Monitor()
    try:
        m.run()
    except KeyboardInterrupt:
        print("Goodbye!")


if __name__ == '__main__':
    sys.exit(main())
