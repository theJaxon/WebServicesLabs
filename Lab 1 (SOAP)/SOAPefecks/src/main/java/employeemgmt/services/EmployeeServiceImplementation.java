package employeemgmt.services;

import employeemgmt.domain.Employee;

import javax.jws.WebService;

@WebService
public class EmployeeServiceImplementation implements EmployeeService {

    @Override
    public Employee getEmployeeById(String id) {
        return new Employee("1", "Jaxon");
    }
    
}
