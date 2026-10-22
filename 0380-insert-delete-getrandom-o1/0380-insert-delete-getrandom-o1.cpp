class RandomizedSet {  
private:
        std::map<int, int>* idx;
        std::vector<int>* vals;
public:
    RandomizedSet() {
        idx = new std::map<int, int>;
        vals = new std::vector<int>;
    }

    bool insert(int val) {
        if(idx->count(val)) return false;
        vals->push_back(val);
        (*idx)[val] = vals->size()-1;
        return true; 
    }
    
    bool remove(int val) {
        if(idx->count(val)){
            int index = (*idx)[val];
            int lastVal = vals->back();
            (*vals)[index] = lastVal;
            (*idx)[lastVal] = index;
            vals->pop_back();
            idx->erase(val);
            return true;
        }
        return false;
    }
    
    int getRandom() {
        std::random_device rd;
        std::mt19937 gen(rd()); 
        std::uniform_int_distribution<> distrib(0, vals->size()-1);
        int n = distrib(gen);
        return (*vals)[n];
    }

    ~RandomizedSet(){
        delete idx;
        delete vals;
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */