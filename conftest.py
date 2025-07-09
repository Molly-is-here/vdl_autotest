import os
import sys
import time
addpath = os.path.dirname(__file__)
if addpath not in sys.path:
    sys.path.append(addpath)

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果并写入 result.txt'''
    total = getattr(terminalreporter, "_numcollected", 0)
    passed = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    failed = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    error = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
    skipped = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])

    if total > 0:
        successful = passed / total * 100
    else:
        successful = 0.0

    duration = time.time() - getattr(terminalreporter, "_sessionstarttime", time.time())

    print('total times: %.2f' % duration, 'seconds')

    result_txt_path = os.path.join(addpath, "result.txt")
    with open(result_txt_path, "w") as fp:
        fp.write(f"TOTAL={total}\n")
        fp.write(f"PASSED={passed}\n")
        fp.write(f"FAILED={failed}\n")
        fp.write(f"ERROR={error}\n")
        fp.write(f"SKIPPED={skipped}\n")
        fp.write(f"SUCCESSFUL={successful:.2f}%\n")
        fp.write(f"TOTAL_TIMES={duration:.2f}s\n")