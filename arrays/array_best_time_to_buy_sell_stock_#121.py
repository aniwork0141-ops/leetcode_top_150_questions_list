'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]

def maxProfit(prices):
    mx = 0
    mn = float('inf') # positive infinity
    for i in range(len(prices)):
      mn = min(mn,prices[i]) #min so far
      mx = max(mx, prices[i] - mn) #profit if sold today
    return mx

print(maxProfit(prices))

# TC - O(n) and SC - O(1) 
### Explanation :
'''
Key idea: Make the loop variable the sell day. Each iteration asks one question: if today is my sell day, what's the best profit I could get? You still try every sell day — nothing is skipped there. The saving is on the buy side: the best buy for a fixed sell day is just the cheapest price before it, which can be carried in one variable instead of rescanned.

Brute force — O(n²), TLE. Written with loops swapped so the structure is visible:

python
for j in range(len(prices)):     # j = SELL day
    for i in range(j):           # i = BUY day, before j
        mx = max(mx, prices[j] - prices[i])

The inner loop only ever computes min(prices[0..j-1]). Replace it with a running minimum → the loop collapses.

Optimized — O(n) time, O(1) space:

python
def maxProfit(prices):
    mn = float('inf')
    mx = 0
    for p in prices:
        mn = min(mn, p)          # cheapest buy so far
        mx = max(mx, p - mn)     # best profit if sold today
    return mx

Trace on [7,1,5,3,6,4]:

p (sell day)	mn	profit	mx
7	7	0	0
1	1	0	0
5	1	4	4
3	1	2	4
6	1	5	5
4	1	3	5

Notes:

Order of the two lines is safe: mn updates first, so on a new-low day you compute p - p = 0, which never beats mx = 0.
mx = 0 is not a placeholder — it's the required answer when no profit exists.
float('inf') over a magic number like 99999: no ceiling to accidentally exceed if constraints change.
Only the buy side has a shortcut. The max price is not necessarily the best sell day — [8,9,1,5]: selling at 9 gives 1, selling at 5 gives 4.

Pattern: single-pass with a running extremum. One accumulator summarizes everything to the left, so each element is visited once. Reuse in Kadane's, container with most water, trapping rain water.
'''
