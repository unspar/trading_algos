
#Thoughts

##Execution

###How to place orders
TODO- Build a system to run the orders with a broker
The system should minimize the work needed to add another broker (wrapper?)


###How to track portfolio state
TODO- the order system should journal all activity into a log for tracking/debugging
The log should be able to recreate the current portfolio


###How to monitor live algos
TODO- develop a framework for killing old algos
TODO - Develop a big red button to stop everything (failsafe)


##Algo design
###How to think about risk
What do I measure myself against? - Other peopel on quantopian? 
If I work there a bit I can get a good sense of what kinds of strategies work.
####Correlation with other factors
You should have a mechanism for testing correlation with other standard factors:
SPY - large cap stocks
VTI - US stock marker
VIX - Risk
Momentum
Cyclical 
Dividend yields
Value 




###How to handle testing and validation
Zipline -> Pyfolio
TODO - Build a backtester like quantopian's for algos


##Data
###Data infrastructure
Servers to hold data? 
Put them in databases?




##Architecture
Before you understand this you should understand Zipline and pyfolio better
There may be technical limitations that prevent this strategy

###Startup
Initially you should have all trades executed by hand. 
Algos shoudl be operating on the day scale (you're slow).
Competative advantage is small size, not advanced trading infrastructure.

###Central control
I want a central server to store all state.
This should be a clustered something.
Options:
- Aerospike
- Cassandra
Goals:
Speed
Consistency
Tolerant to single-instance failures
Cross data center replication (available)


###Workers to run individual strategies
I'm thinking of worker servers to run the strategies
Probelems:
- How to centralize data for testing/trading?
- Communication with central engine

