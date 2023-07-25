```python
import numpy as np

class DecisionManagementLogic:
    def __init__(self):
        self.dml_model = None

    def load_model(self, model_path):
        """
        Load the pre-trained DML model
        """
        self.dml_model = np.load(model_path)

    def decision_logic(self, threat_severity, cost_of_remediation, business_impact):
        """
        Make decisions based on the severity of the threat, cost of remediation, and business impact
        """
        if self.dml_model is None:
            raise Exception("Model not loaded. Please load the model first.")

        # Normalize the inputs
        threat_severity = self._normalize(threat_severity, 0, 10)
        cost_of_remediation = self._normalize(cost_of_remediation, 0, 10000)
        business_impact = self._normalize(business_impact, 0, 100)

        # Use the DML model to make a decision
        decision = self.dml_model.predict([threat_severity, cost_of_remediation, business_impact])

        return decision

    def _normalize(self, value, min_value, max_value):
        """
        Normalize a value to the range [0, 1]
        """
        return (value - min_value) / (max_value - min_value)

if __name__ == "__main__":
    dml = DecisionManagementLogic()
    dml.load_model("dml_model.npy")
    decision = dml.decision_logic(7, 5000, 50)
    print(f"Decision: {decision}")
```