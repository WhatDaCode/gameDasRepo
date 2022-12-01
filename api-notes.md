# Fetch data from [API](https://developer.riotgames.com/apis)
***
#### Fetch Basic Information (summoner-v4)
**GET** -  `/lol/summoner/v4/summoners/by-name/{summonerName}`

**Parameters:** `summonerName` - String - Summoner Name
**Return value: SummonerDTO**

*SummonerDTO - represents a summoner*

| NAME      | DATA TYPE  | DESCRIPTION     |
| :---       |    :----:   |          :--- |
| accountId      | string       | Encrypted account ID. Max length 56 characters.   |
|profileIconId | int |	ID of the summoner icon associated with the summoner.|
|revisionDate |	long | Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: summoner name change, summoner level change, or profile icon change.
|name|	string|	Summoner name.|
| id	| string |	Encrypted summoner ID. Max length 63 characters.|
|puuid	|string|	Encrypted PUUID. Exact length of 78 characters.|
|summonerLevel	|long|	Summoner level associated with the summoner.|


#### Fetch Summoner Ranks (league-v4)
**GET** -  `/lol/league/v4/entries/by-summoner/{encryptedSummonerId}`

**Parameters:** `encryptedSummonerId` - String - Summoner Id
**Return value: Set[LeagueEntrryDTO]**


| NAME      | DATA TYPE  | DESCRIPTION     |
| :---       |    :----:   |          :--- |
| leagueId      | string       |    |
|summonerId | string |	Player's encrypted summonerId.|
|summonerName |	string | |
|queueType|	string|	|
| tier	| string |	|
|rank	|string|	The player's division within a tier.|
|leaguePoints	|int|  |
|wins|	int	|Winning team on Summoners Rift.|
|losses|	int|	Losing team on Summoners Rift.|
|hotStreak|	boolean|
|veteran|	boolean|
|freshBlood| boolean|
|inactive|	boolean|
|miniSeries| `MiniSeriesDTO` |

MiniSeriesDTO
| NAME      | DATA TYPE  | DESCRIPTION     |
| :---       |    :----:   |          :--- |
|losses|int| |
|progress|string| |
|target|int| |
|wins|int| |



## Errors Codes


|HTTP STATUS CODE | REASON | 
| :--- | :---|
|400	|Bad request|
|401	|Unauthorized|
|403|	Forbidden|
|404|	Data not found|
|405|	Method not allowed|
|415|	Unsupported media type|
|429|	Rate limit exceeded|
|500|	Internal server error|
|502|	Bad gateway|
|503|	Service unavailable|
|504|	Gateway timeout|
