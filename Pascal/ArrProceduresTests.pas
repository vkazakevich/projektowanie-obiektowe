unit ArrProceduresTests;

interface 

uses
   TestFramework, 
   Math,
   ArrProcedures;

type
   TTestArrProcedures = class(TTestCase)
   published    
      procedure TestFillRandomIntArrMaxAllowed;
      procedure TestFillRandomIntArrMinAllowed;
      procedure TestFillRandomIntArr;

      procedure TestBubbleSortReversedArr;
      procedure TestBubbleSort;
   end;

procedure RegisterTests;

implementation

procedure RegisterTests;
begin
   TestFramework.RegisterTest(TTestArrProcedures.Suite);
end;

procedure TTestArrProcedures.TestFillRandomIntArrMaxAllowed;

var
   randomArr : IntArray;
   min, max : integer;

begin
   SetLength(randomArr, 100);
   min := 10;
   max := 1;

   StartExpectingException(EInvalidArgument);
   FillRandomIntArr(randomArr, min, max);
   StopExpectingException();
end;

procedure TTestArrProcedures.TestFillRandomIntArrMinAllowed;

var
   randomArr : IntArray;
   min, max : integer;

begin
   SetLength(randomArr, 100);
   min := -10;
   max := 10;

   StartExpectingException(EInvalidArgument);
   FillRandomIntArr(randomArr, min, max);
   StopExpectingException();
end;

procedure TTestArrProcedures.TestFillRandomIntArr;

const 
   size = 10;

var
   arr : IntArray;
   min, max, i : integer;

begin
   SetLength(arr, size);
   min := 5;
   max := 10;

   for i := 0 to size - 1 do
      CheckEquals(arr[i], 0);

   FillRandomIntArr(arr, min, max);

   for i := 0 to size - 1 do
      CheckNotEquals(arr[i], 0);
end;

procedure TTestArrProcedures.TestBubbleSortReversedArr;

var 
   arr : array[0..50] of integer;
   arr2 : array[0..50] of integer;
   i : integer;

begin
   for i := 0 to 50 do begin
      arr[i] := 50 - i;
      arr2[i] := i;
   end;
   
   for i := 0 to 50 do
      CheckEquals(arr[i], 50 - arr2[i]);

   BubbleSort(arr);

   for i := 0 to 50 do
      CheckEquals(arr[i], arr2[i]);
end;

procedure TTestArrProcedures.TestBubbleSort;

var 
   arr : array[0..10000] of integer;
   i : integer;

begin
   Randomize;

   for i := 0 to 10000 do begin
      arr[i] := Random(10000000);
   end;

   BubbleSort(arr);
   
   CheckEquals(arr[0], MinIntValue(arr));
   CheckEquals(arr[10000], MaxIntValue(arr));
end;

               
initialization
end.
