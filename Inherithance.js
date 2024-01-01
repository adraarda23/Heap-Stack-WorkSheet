function Animal(name) {
    this.name = name;
  }
  
  Animal.prototype.sayHello = function () {
    console.log(`Hello, I'm ${this.name}`);
  };
  
  function Dog(name, breed) {
    Animal.call(this, name);
    this.breed = breed;
  }
  
  Dog.prototype = Object.create(Animal.prototype);
  Dog.prototype.constructor = Dog;
  
  Dog.prototype.bark = function () {
    console.log("Woof, woof!");
  };
  
  const myDog = new Dog('Buddy', 'Golden Retriever');
  myDog.sayHello();
  myDog.bark();
  