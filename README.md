# berthlane

Three independent terminal services in one repository.

| Service | Responsibility | Tests |
|---|---|---|
| `services/gatein` | Truck gate-in lane assignment | 4 |
| `services/yardmap` | Yard slot allocation | 4 |
| `services/railout` | Rail departure planning | 4 |

Each service is self-contained: its own `src/` and `tests/`, no shared
imports. A change to one does not affect the others — which is the point
of testing them selectively rather than all together.

## Tests

```
pytest services/gatein/tests -q
pytest services/yardmap/tests -q
pytest services/railout/tests -q
```


##
Twelve tests across three services that share no code. As of right now any changes would run all twelve. By the end of the hour a push that touches one service will run only that service's test, and I will be able to show the others were never even scheduled.


## 
Update on the work. The test shows twenty rows by five tiers which is a hundred slots, and the test still expects eighty. The failure names the exact value, so the test is pinning real behaviour rather than just existing

## 
Four restored tests ran, not 12, even putting things back only costs the work the change actually implies. 
