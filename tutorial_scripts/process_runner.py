from subprocess import Popen
import glob

test_cases = glob.glob('test*.py')
processes = []
for test in test_cases:
	processes.append(Popen('python %s' % test, shell=True))
for process in processes:
	process.wait()
