"""
Launch the Reparent window.
"""

import os
import sys

# Ensure that '<root>/python'  is on the PYTHONPATH
path = os.path.dirname(__file__)
package_path = os.path.abspath(os.path.join(path, 'python'))
sys.path.insert(0, package_path)

if __name__ == '__main__':
    import qtLearn.windows.examples.exampleSuggestionsPopup
    qtLearn.windows.examples.exampleSuggestionsPopup.main(sys.argv)

