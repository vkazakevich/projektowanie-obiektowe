program Randomizer;

const
   size = 50;

type 
   IntArray = Array [0..size] of Integer;

var 
   randomArr : IntArray;
   i : Integer;

procedure RandomIntArr(var arr: IntArray);   

begin
   Randomize;

   for i:= 0 to size do
      arr[i] := Random(100);
end;

begin
   RandomIntArr(randomArr);
   writeln(randomArr[0], ' ', randomArr[50]);
end. 
