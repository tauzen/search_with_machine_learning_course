### How many unique categories did you see in your rolled up training data when you set the minimum number of queries per category to 1000? To 10000?

* min queries 1000 - 387 categories
* min queries 10000 - 69 categories

### What were the best values you achieved for R@1, R@3, and R@5? You should have tried at least a few different models, varying the minimum number of queries per category, as well as trying different fastText parameters or query normalization. Report at least 2 of your runs.

All runs avaialable in evaluation.md
Two best runs:

* `min_queries=1000`, trainig data size = 50 000, `lr=0.6`, `epochs=25`, `wordNgrams=2`
   * R@1 0.5263
   * R@3 0.7136
   * R@5 0.7757
* `min_queries=1000`, trainig data size = 100 000, `lr=0.6`, `epochs=25`, `wordNgrams=2`
   * R@1 0.5437
   * R@3 0.741
   * R@5 0.8024

### Give 2 or 3 examples of queries where you saw a dramatic positive change in the results because of filtering. Make sure to include the classifier output for those queries

* iphone 4
  * without filtering top 3:
    * ZAGG - InvisibleSHIELD HD ...
    * LifeProof - Case for Apple ...
    * ZAGG - InvisibleSHIELD for Apple ...
  * with filtering top 3:
    * Apple - iPhone 4 with 8GB Memory - White (AT&T)
    * Apple - iPhone 4 with 8GB Memory - White (Verizon Wireless)
    * Apple - iPhone 4 with 8GB Memory - Black (AT&T)
* touchpad
  * without filtering top 3
    * Logitech - M325 Mouse
    * Logitech - M325 Mouse
    * Logitech - K400 Keyboard
  * with filtering top 3
    * HP - TouchPad Tablet with 16GB Memory - Black
    * HP - Refurbished Touchpad Tablet with 16GB Memory - Black
    * HP - Refurbished Touchpad Tablet with 32GB Memory - Black

### Give 2 or 3 examples of queries where filtering hurt the results, either because the classifier was wrong or for some other reason. Again, include the classifier output for those queries.

* nokia
  * without filtering - not great but at least I got one nokia phone, couple of cases, chargers and a nokia camer headset
  * with filtering - got only batteries to Nokia phones
