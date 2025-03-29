program Randomizer;

uses
   ArrProcedures;

var
   randomArr : IntArray;
   min, max, size : integer;

begin
   repeat
      Writeln('Write MIN random number (min 0):');
      Readln(min)
   until
      (min >= 0);

   repeat
      Writeln('Write MAX random number (min ', (min + 1),'):');
      Readln(max)
   until
      (max > min);

   repeat
      Writeln('Write count of random numbers (min 1):');
      Readln(size)
   until
      (size > 0);

   setLength(randomArr, size);

   RandomIntArr(randomArr, size, min, max);
   DisplayArr(randomArr, size);

   SortArr(randomArr, size);
   DisplayArr(randomArr, size);
end. 
