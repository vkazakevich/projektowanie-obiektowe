program TestRunner;

uses
   TextTestRunner,
   ArrProceduresTests;

begin
   ArrProceduresTests.RegisterTests;
   RunRegisteredTests;
end.