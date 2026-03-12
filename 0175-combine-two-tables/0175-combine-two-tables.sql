
select 
    p.firstName,
    p.lastName,
    a.city,
    a.state
From Person p
left join Address a ON p.personId = a.personId;    