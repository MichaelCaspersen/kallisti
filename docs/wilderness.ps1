$rooms = import-csv "C:\Users\Gamer\Downloads\wilderness_rooms-komma.csv"

foreach($room in $rooms) {

$VNUM = $room.vnum
$WEST = $room.w
$EAST = $room.e
$SOUTH = $room.s
$NORTH = $room.n

$text = "R {$VNUM} {0} {<178>} {room-name} {-} {} {The Wilderness} {} {Unknown} {} {1.000} {}`r`n

E {$NORTH} {n} {n} {1} {0} {} {1.000} {} {0.00}`r`n
E {$SOUTH} {s} {s} {4} {0} {} {1.000} {} {0.00}`r`n
E {$EAST} {e} {e} {2} {0} {} {1.000} {} {0.00}`r`n
E {$WEST} {w} {w} {8} {0} {} {1.000} {} {0.00}`r`n
`r`n"


write-output $text  | add-content "C:\Users\Gamer\Downloads\wilderness_rooms.txt"

}