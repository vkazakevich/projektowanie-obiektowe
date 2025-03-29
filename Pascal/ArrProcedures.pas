unit ArrProcedures;

interface

type 
   IntArray = array of integer;

procedure RandomIntArr(var arr: IntArray; arrSize: integer; min: integer; max: integer);
procedure SortArr(var arr: IntArray; arrSize: integer);
procedure DisplayArr(var arr: IntArray; arrSize: integer);

implementation

procedure RandomIntArr(var arr: IntArray; arrSize: integer; min: integer; max: integer);   

var i : integer;

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

var i : integer;

begin
   Writeln('Result:');
   for i := 1 to arrSize do
      write(arr[i], ' ');
   Writeln;
end;

initialization
end.