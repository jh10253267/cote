select count(*) as FISH_COUNT, MONTH(time) as MONTH from fish_info group by month(time)
order by MONTH