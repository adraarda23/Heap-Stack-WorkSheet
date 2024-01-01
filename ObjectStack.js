function createObject() {
    return { prop1: 'value1', prop2: 'value2' };
  }
  
  function modifyObject(obj) {
    obj.prop1 = 'modifiedValue1';
    obj.newProp = 'newValue';
  }
  
  function testObjectLocation() {
    const obj1 = createObject();
    const obj2 = { prop1: 'value1', prop2: 'value2' };
    
    modifyObject(obj1);
  
    // Garbage collection might occur here
  
    modifyObject(obj2);
  
    console.log(obj1);
    console.log(obj2);
  }
  
  testObjectLocation();
  