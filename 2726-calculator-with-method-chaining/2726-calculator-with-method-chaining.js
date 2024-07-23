class Calculator {
    
    /** 
     * @param {number} value
     */
    // int result;
    constructor(value) {
        this.result = value;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    add(value){
        return new Calculator(this.result + value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    subtract(value){
        return new Calculator(this.result - value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */  
    multiply(value) {
        return new Calculator(this.result * value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    divide(value) {
        if(value == 0) {
            return new Calculator("Division by zero is not allowed");
        }
        return new Calculator(this.result / value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    power(value) {
        return new Calculator(Math.pow(this.result, value));
    }
    
    /** 
     * @return {number}
     */
    getResult() {
        return this.result;
    }
}