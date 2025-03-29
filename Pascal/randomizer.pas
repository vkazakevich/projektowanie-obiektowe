program Randomizer;

type 
   IntArray = array of integer;

var
   randomArr : IntArray;
   i : integer;
   min, max, size : integer;

procedure RandomIntArr(var arr: IntArray; arrSize: integer; min: integer; max: integer);   

begin
   Randomize;

   for i:= 1 to arrSize do
      arr[i] := Random(max - min + 1) + min;
end;

procedure SortArr(var arr: IntArray; arrSize: integer);

var
   i, j, temp : integer;

begin
   for i := 1 to arrSize - 1 do
      for j := 1 to arrSize - 1 do
         if arr[j] > arr[j + 1] then begin
            temp := arr[j];
            arr[j] := arr[j + 1];
            arr[j + 1] := temp;
         end;
end;

procedure DisplayArr(var arr: IntArray; arrSize: integer);   

begin
   Writeln('Result:');
   for i := 1 to arrSize do
      write(randomArr[i], ' ');
   Writeln;
end;

begin
   Writeln('Write MIN random number (min 0):');
   Readln(min);

   if (min < 0) then begin
      Writeln('Validation Error: MIN must be greater than 0.');
      Halt (1);
   end;

   Writeln('Write MAX random number (min ', (min + 1),'):');
   Readln(max);

   if (min > max) then begin
      Writeln('Validation Error: MAX must be greater than MIN.');
      Halt (1);
   end;

   Writeln('Write count of random numbers (min 1):');
   Readln(size);

   if (size < 1) then begin
      Writeln('Validation Error: Count of random numbers must be greater than 0.');
      Halt (1);
   end;

   setLength(randomArr, size);

   RandomIntArr(randomArr, size, min, max);
   DisplayArr(randomArr, size);

   SortArr(randomArr, size);
   DisplayArr(randomArr, size);
end. 
