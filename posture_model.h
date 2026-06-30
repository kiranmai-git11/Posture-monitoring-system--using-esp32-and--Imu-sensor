#pragma once
#include <EloquentTinyML.h>
namespace Eloquent {
    namespace ML {
        namespace Port {
            class DecisionTree {
            public:
                int predict(float *x) {
                    if (x[0] <= -4000) {
                        return 0;   // Bending Backward
                    }
                    else if (x[0] >= 4000) {
                        return 1;   // Bending Forward
                    }
                    else if (x[1] <= -4000) {
                        return 2;   // Bending Left
                    }
                    else if (x[1] >= 4000) {
                        return 3;   // Bending Right
                    }
                    else if (x[2] <= -4000) {
                        return 5;   // Twisting Left
                    }
                    else if (x[2] >= 4000) {
                        return 6;   // Twisting Right
                    }
                    else {
                        return 4;   // Normal
                    }
                }
            };
        }
    }
}
