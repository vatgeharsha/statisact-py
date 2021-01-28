import unittest,math
import statistics

class EmailAlert():
    def __init__(self):
        self.emailSent = False
class LEDAlert():
    def __init__(self):
        self.ledGlows = False
class StatsAlerter():
    def __init__(self,v1,v2):
        self.maxThreshold = v1
        self.list = v2
    def checkAndAlert(self,v):
        val = max(v)
        if val > self.maxThreshold:
            self.list[0].emailSent = True
            self.list[1].ledGlows = True
            
        
class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    val = [1.5, 8.9, 3.2, 4.5]
    computedStats = statistics.calculateStats(val)
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Design the assert here.
    # Use nan and isnan in https://docs.python.org/3/library/math.html
    self.assertTrue(math.isnan(computedStats))

  def test_raise_alerts_when_max_above_threshold(self):
    emailAlert = EmailAlert()
    ledAlert = LEDAlert()
    maxThreshold = 10.5
    statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
    statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
    self.assertTrue(emailAlert.emailSent)
    self.assertTrue(ledAlert.ledGlows)

if __name__ == "__main__":
    unittest.main()
