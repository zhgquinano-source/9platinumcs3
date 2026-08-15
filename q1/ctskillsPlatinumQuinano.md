# Computational Thinking Exercise
## [Smart School Canteen Queue]
**Name:** Zach Henrie
**Section:** Platinum
**Last Name:** Quinano
**Date:** 08/15/26
---

## Step 1: Identify the Big Problem
### Main Problem
The PSHS school canteen ordering and payment process is slow and inefficient, leading to heavy crowding and long lines during lunch break 
---
## Step 2: Identify the Sub-Problems
1. Students take too long to view the available menu options and decide what food to buy at the counter.
2. Cashiers lose time manually calculating total costs and making physical change for payments.
3. Staff has no automated system to monitor food stock levels, leading to unexpected sell-outs and confusion.
4. High student density in a small place creates restriction without organized line flow or pre-ordering.
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Ordering inefficiency | Abstraction | A digital menu board showing only item names, prices, and stock status. |
| Manual transaction delays | Algorithmic Thinking | POS system that automatically calculates totals, change, or accepts card payments. |
| Lack of inventory tracking | Pattern Recognition | Auto-deduct inventory per sale and alert staff when stock runs low. |
| Physical space & queue management | Decomposition | Separate the line into pre-ordering, payment, and pickup stations. |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Manual transaction delays
### Pseudocode
START
SET total_cost = 0
  
  WHILE student is adding items DO
    INPUT item_price
    total_cost = total_cost + item_price
  END WHILE
  
  DISPLAY total_cost
  
  INPUT payment_amount
  
  IF payment_amount >= total_cost THEN
    change_due = payment_amount - total_cost
    DISPLAY "Transaction Successful"
    DISPLAY "Change Due: " + change_due
  ELSE
    DISPLAY " insufficient payment, please pay the total amount"
  END IF
END
---
