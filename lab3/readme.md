input:

`entry {
    int number;

    number = 3;

    if(number > 5) {
        WRITE("SARMALE");
    }
}`

ST is:
`[]
[['number', 0], ['3', 0]]
[]
[['5', 0], ['SARMALE', 0]]`

PIF is:
`('entry', 0)
('{', 0)
('int', 0)
('number', 0)
(';', 0)
('=', 0)
('3', 1)
(';', 0)
('if', 0)
('(', 0)
('>', 0)
('5', 0)
(')', 0)
('{', 0)
('WRITE', 0)
('(', 0)
('"', 0)
('SARMALE', 1)
('"', 0)
(')', 0)
(';', 0)
('}', 0)
('}', 0)`

