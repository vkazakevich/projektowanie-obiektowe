program Randomizer;

const
   size = 50;

type 
   IntArray = Array [1..size] of Integer;

var 
   randomArr : IntArray;
   i : Integer;

procedure RandomIntArr(var arr: IntArray);   

begin
   Randomize;

   for i:= 1 to size do
      arr[i] := Random(100);
end;

procedure SortArr(var arr: IntArray);

var
   arrSize : Integer;
   i, j, temp : Integer;

begin
   arrSize := Length(arr);

   for i := 1 to arrSize - 1 do
      for j := 1 to arrSize - 1 do
         if arr[j] > arr[j + 1] then begin
            temp := arr[j];
            arr[j] := arr[j + 1];
            arr[j + 1] := temp;
         end;
end;

procedure DisplayArr(var arr: IntArray);   

begin
   for i := 1 to size do
      write(randomArr[i], ' ');
   writeln;
end;

begin
   RandomIntArr(randomArr);
   DisplayArr(randomArr);

   SortArr(randomArr);
   DisplayArr(randomArr);
end. 
