# dslabmongo

Step 7.
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T20:23:52.806Z"),
	"myState" : 1,
	"term" : NumberLong(1),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572639822, 1),
			"t" : NumberLong(1)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T20:23:42.990Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572639822, 1),
			"t" : NumberLong(1)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T20:23:42.990Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572639822, 1),
			"t" : NumberLong(1)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572639822, 1),
			"t" : NumberLong(1)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T20:23:42.990Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T20:23:42.990Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572639792, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572639792, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "electionTimeout",
		"lastElectionDate" : ISODate("2019-11-01T19:33:12.111Z"),
		"termAtElection" : NumberLong(1),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(0, 0),
			"t" : NumberLong(-1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572636781, 1),
			"t" : NumberLong(-1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"numCatchUpOps" : NumberLong(1702132066),
		"newTermStartDate" : ISODate("2019-11-01T19:33:12.904Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T19:33:13.786Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "172.31.38.199:27017",
			"ip" : "172.31.38.199",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 3468,
			"optime" : {
				"ts" : Timestamp(1572639822, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T20:23:42Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572636792, 1),
			"electionDate" : ISODate("2019-11-01T19:33:12Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 1,
			"name" : "172.31.17.159:27017",
			"ip" : "172.31.17.159",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 3050,
			"optime" : {
				"ts" : Timestamp(1572639822, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572639822, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T20:23:42Z"),
			"optimeDurableDate" : ISODate("2019-11-01T20:23:42Z"),
			"lastHeartbeat" : ISODate("2019-11-01T20:23:51.655Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T20:23:50.959Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "172.31.38.199:27017",
			"syncSourceHost" : "172.31.38.199:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 2,
			"name" : "172.31.17.238:27017",
			"ip" : "172.31.17.238",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 3050,
			"optime" : {
				"ts" : Timestamp(1572639822, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572639822, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T20:23:42Z"),
			"optimeDurableDate" : ISODate("2019-11-01T20:23:42Z"),
			"lastHeartbeat" : ISODate("2019-11-01T20:23:51.655Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T20:23:50.959Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "172.31.38.199:27017",
			"syncSourceHost" : "172.31.38.199:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572639822, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572639822, 1)
}

rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "172.31.38.199:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "172.31.17.159:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "172.31.17.238:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5dbc886dcd1a884a526ab19c")
	}
}

Step 8.
![alt text](https://github.com/liarmand/dslabmongo/blob/master/Снимок%20экрана%202019-11-01%20в%2023.19.22.png)


Step 10.1.
rs0:SECONDARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T20:35:38.042Z"),
	"myState" : 2,
	"term" : NumberLong(2),
	"syncingTo" : "172.31.17.159:27017",
	"syncSourceHost" : "172.31.17.159:27017",
	"syncSourceId" : 1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572640531, 1),
			"t" : NumberLong(2)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T20:35:31.406Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572640531, 1),
			"t" : NumberLong(2)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T20:35:31.406Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572640531, 1),
			"t" : NumberLong(2)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572640531, 1),
			"t" : NumberLong(2)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T20:35:31.406Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T20:35:31.406Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572640508, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572640508, 1),
	"members" : [
		{
			"_id" : 0,
			"name" : "172.31.38.199:27017",
			"ip" : "172.31.38.199",
			"health" : 0,
			"state" : 8,
			"stateStr" : "(not reachable/healthy)",
			"uptime" : 0,
			"optime" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDate" : ISODate("1970-01-01T00:00:00Z"),
			"optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
			"lastHeartbeat" : ISODate("2019-11-01T20:35:36.972Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T20:32:35.920Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "Couldn't get a connection within the time limit",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"configVersion" : -1
		},
		{
			"_id" : 1,
			"name" : "172.31.17.159:27017",
			"ip" : "172.31.17.159",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 3755,
			"optime" : {
				"ts" : Timestamp(1572640531, 1),
				"t" : NumberLong(2)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572640531, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-11-01T20:35:31Z"),
			"optimeDurableDate" : ISODate("2019-11-01T20:35:31Z"),
			"lastHeartbeat" : ISODate("2019-11-01T20:35:37.482Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T20:35:37.321Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572640357, 1),
			"electionDate" : ISODate("2019-11-01T20:32:37Z"),
			"configVersion" : 1
		},
		{
			"_id" : 2,
			"name" : "172.31.17.238:27017",
			"ip" : "172.31.17.238",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 4208,
			"optime" : {
				"ts" : Timestamp(1572640531, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-11-01T20:35:31Z"),
			"syncingTo" : "172.31.17.159:27017",
			"syncSourceHost" : "172.31.17.159:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572640531, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572640531, 1)
}

Step 10.2.
rs0:SECONDARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "172.31.38.199:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "172.31.17.159:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "172.31.17.238:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5dbc886dcd1a884a526ab19c")
	}
}

Step 10.3.
![alt text](https://github.com/liarmand/dslabmongo/blob/master/Снимок%20экрана%202019-11-01%20в%2023.46.18.png)



