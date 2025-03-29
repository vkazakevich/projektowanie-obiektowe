unit ArrProcedures;

{$mode objfpc}

interface

uses SysUtils;

type 
   IntArray = array of integer;
   EInvalidArgument = Exception;

procedure FillRandomIntArr(var arr: array of integer; min: integer; max: integer);
procedure BubbleSort(var arr: array of integer);
procedure DisplayArr(var arr: array of integer);

implementation

procedure FillRandomIntArr(var arr: array of integer; min: integer; max: integer);   

var i : integer;

begin
   Randomize;

   if min < 0 then
      raise EInvalidArgument.create('MIN must be more than 0.');

   if min > max then
      raise EInvalidArgument.create('MAX must be more than MIN.');

   for i:= 0 to Length(arr) - 1 do
      arr[i] := Random(max - min + 1) + min;
end;

procedure BubbleSort(var arr: array of integer);

var i, j, temp, size : integer;

begin
   size := Length(arr) - 1;

   for i := 0 to size - 1 do
      for j := 0 to size - 1 do
         if arr[j] > arr[j + 1] then begin
            temp := arr[j];
            arr[j] := arr[j + 1];
            arr[j + 1] := temp;
         end;
end;

procedure DisplayArr(var arr: array of integer);   

var i : integer;

begin
   Writeln('Result:');
   for i := 0 to Length(arr) - 1 do
      write(arr[i], ' ');
   Writeln;
end;

initialization
end.