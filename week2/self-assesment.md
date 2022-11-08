### 1. For classifying product names to categories:

#### What precision (P@1) were you able to achieve?
`P@1     0.957`

#### What fastText parameters did you use?
`lr=1.0, epoch=25, wordNgrams=2`

#### How did you transform the product names?
CLI normalization command from the assignment

#### How did you prune infrequent category labels, and how did that affect your precision?
`categories_counter[category] >= 500`

#### How did you prune the category tree, and how did that affect your precision?
x

### 2. For deriving synonyms from content:

#### What were the results for your best model in the tokens used for evaluation?
```
In [3]: model.get_nearest_neighbors("iphone")
Out[3]: 
[(0.8329026103019714, '4s'),
 (0.8012158274650574, '3gs'),
 (0.7946497201919556, 'apple'),
 (0.7695806622505188, '3g'),
 (0.7420698404312134, 'ifrogz'),
 (0.6656878590583801, 'luxe'),
 (0.6583127975463867, 'hardshell'),
 (0.6575022339820862, 'incase'),
 (0.6561269164085388, 'belkin'),
 (0.6548761129379272, 'silicone')]
 ```

#### What fastText parameters did you use?
`-epoch 25`

#### How did you transform the product names?
CLI normalization command from the assignment

### 3. For integrating synonyms with search:

#### How did you transform the product names (if different than previously)?
CLI normalization command from the assignment

#### What threshold score did you use?
`0.75`

#### Were you able to find the additional results by matching synonyms?
Yes, except for nespresso (didn't have synonyms for it)