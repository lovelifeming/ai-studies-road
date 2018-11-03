package com.zsm.jython.python;

import com.alibaba.fastjson.JSONObject;
import org.python.core.*;
import org.python.util.PythonInterpreter;

import java.io.*;


/**
 * @Author: zengsm.
 * @Description: TODO()
 * @Date:Created in 2018/9/27.
 * @Modified By:
 */
public class Jython
{
    public static void main(String[] args)
        throws IOException, InterruptedException
    {
        invokePython();
//        invokeRuntime();
//        execPython();
    }

    /**
     * 在Java中通过Runtime调用Python程序与直接执行Python程序的效果是一样的.需要注意的是，不能在Python中通过return语句返回结果，
     * 只能将返回值写入到标准输出流中，然后在Java中通过标准输入流读取Python的输出值。
     *
     * @throws IOException
     * @throws InterruptedException
     */
    public static void invokeRuntime()
    {
        String exec = "python";
        String command = "D:\\jython\\test.py";
        String num1 = "1";
        String num2 = "2";
        String[] cmd = new String[] {exec, command, num1, num2};
        Process process = null;
        try
        {
            process = Runtime.getRuntime().exec(cmd);
            InputStream is = process.getInputStream();
            BufferedReader in = new BufferedReader(new InputStreamReader(is));
            String line;
            while ((line = in.readLine()) != null)
            {
                String result = line;
                System.out.println(result);
            }
            in.close();
            process.waitFor();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        finally
        {
            process.destroy();
        }
        /** Python 代码
         *  from sys import argv
         *  num1 = argv[1]
         *  num2 = argv[2]
         *  sum = int(num1) + int(num2)
         *  print(sum)
         */
    }

    /**
     * 直接执行python脚本
     */
    public static void invokePython()
    {
        PythonInterpreter interpreter = new PythonInterpreter();
        PySystemState state = Py.getSystemState();
        state.path.add("D:\\Program Files\\Entertainment\\Python\\Lib");
        String code = "def transPython(str):  return str";
        interpreter.exec(code);
        PyFunction func = interpreter.get("transPython", PyFunction.class);
        String str = "{\"CityId\":1,\"CityName\":\"chengdu\",\"ProvinceId\":11,\"CityOrder\":0}";
        PyObject object = func.__call__(new PyString(str));
        JSONObject json = JSONObject.parseObject(object.toString());
        System.out.println(json);
    }

    public static void execPython()
        throws IOException
    {
        //直接执行Python语句
        //PythonInterpreter interpreter = new PythonInterpreter();
        //interpreter.exec("days=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')");
        //for (int i = 0; i < 7; i++)
        //{
        //    interpreter.exec(String.format("print days[%d];", i));
        //}
        /**
         * 输出：Monday         Tuesday         Wednesday         Thursday         Friday         Saturday         Sunday
         */

        //java调用python脚本
        PythonInterpreter interpreter1 = new PythonInterpreter();
        interpreter1.execfile("D:\\jython\\test.py");
        PyFunction func = interpreter1.get("connectStr", PyFunction.class);
        int a = 2018, b = 2;
        PyObject pyobj = func.__call__(new PyInteger(a), new PyInteger(b));
        System.out.println(pyobj.toString());
        /**
         * def connectStr(a, b):
         * return a + b
         *
         * 输出：2020
         */

        //java直接调用python脚本
        PythonInterpreter interpreter2 = new PythonInterpreter();
        BufferedReader in = new BufferedReader(new InputStreamReader(new FileInputStream("D:\\test.txt")));
        interpreter2.setIn(in);
        FileOutputStream out = new FileOutputStream(new File("D:\\test1.txt"));
        //脚本 print 输出流
        interpreter2.setOut(out);
        interpreter2.execfile("D:\\jython\\test.py");
        String line;
        while ((line = in.readLine()) != null)
        {
            String result = line;
            System.out.println("result:" + result);
        }
        in.close();
        interpreter2.cleanup();
        interpreter2.close();

        /**
         * print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
         *
         * 输出：['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
         */

        // 2. 面向对象式编程: 在Java中调用Python对象实例的方法
        String pythonClass = "D:\\calculator_clazz.py";
        // python对象名
        String pythonObjName = "cal";
        // python类名
        String pythonClazzName = "Calculator";
        PythonInterpreter pi2 = new PythonInterpreter();
        // 加载python程序
        pi2.execfile(pythonClass);
        // 实例化python对象
        pi2.exec(pythonObjName + "=" + pythonClazzName + "()");
        // 获取实例化的python对象
        PyObject pyObj = pi2.get(pythonObjName);
        // 调用python对象方法,传递参数并接收返回值
        PyObject result = pyObj.invoke("power", new PyObject[] {Py.newInteger(2), Py.newInteger(3)});
        double power = Py.py2double(result);
        System.out.println(power);

        pi2.cleanup();
        pi2.close();

        /**
         * class Calculator(object):
         * # 计算x的y次方
         * def power(self, x, y):
         * return math.pow(x, y)
         */
    }
}
