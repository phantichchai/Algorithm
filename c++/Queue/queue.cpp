#include <vector>

using namespace std;

class MyQueue {
public:
    MyQueue() {
        // create an empty vector for queue
        q = vector<int>();
    }
    
    void push(int x) {
        // push x value in the back of the queue
        this->q.push_back(x);
    }
    
    int pop() {
        // check queue is empty
        if (this->q.empty()){
            return -1;
        }
        // store the first value of the queue to value varible
        int value = this->q[0];
        // remove the first value of the queue
        this->q.erase(this->q.begin());
        // return value
        return value;
    }
    
    int peek() {
        // check queue is empty
        if (this->q.empty()){
            return -1;
        }
        // return the first value of the queue
        return this->q[0];
    }
    
    bool empty() {
        // return the queue is empty as a boolean
        return this->q.empty();
    }
private:
    vector<int> q;
};
