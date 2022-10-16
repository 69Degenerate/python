from ast import Break
import pymongo
print('-------------emp data insertion script---------------------')
if __name__ == "__main__":
    c=pymongo.MongoClient('mongodb://127.0.0.1:27017')
    print('connected',c)
    db=c['workdb']
    coll=db['emp']
    init=0
    while init==0:
        empno=int(input('enter empno:'))
        enaem=input('enter ename:')
        job=input('enter job :')
        mgr=int(input('enter manager number:'))
        hiredate=input('enter hiredate (dd-mm-yy):')
        sal=int(input('enter salary:'))
        comm=int(input('enter commision:'))
        deptno=int(input('enter department number:'))
        dict=  {
            'empno': empno,
            'ename': enaem,
            'job': job,
            'mgr': mgr,
            'hiredate': hiredate,
            'sal': sal,
            'comm': comm,
            'deptno': deptno
        }
        coll.insert_one(dict)
        ans=input('insert more data(yes/no):')
        if ans=='yes':
            pass
        else:
            break
    for emp in coll.find():
        print(emp)
        
    # coll.delete_many({'empno':7})
    
    # for emp in coll.find():
    #     print(emp)