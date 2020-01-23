from flask import request, render_template, redirect, url_for
from project import app
from project.com.dao.AreaDAO import AreaDAO
from project.com.vo.AreaVO import AreaVO


@app.route('/admin/loadArea', methods=['GET'])
def adminLoadArea():
    try:
        return render_template('admin/addArea.html')
    except Exception as ex:
        print(ex)


@app.route('/admin/insertArea', methods=['POST'])
def adminInsertArea():
    try:
        areaName = request.form['areaName']
        areaPincode = request.form['areaPincode']

        areaVO = AreaVO()
        areaDAO = AreaDAO()

        areaVO.areaName = areaName
        areaVO.areaPincode = areaPincode

        areaDAO.insertArea(areaVO)

        return redirect(url_for('adminViewArea'))
    except Exception as ex:
        print(ex)


@app.route('/admin/viewArea', methods=['GET'])
def adminViewArea():
    try:
        areaDAO = AreaDAO()
        areaVOList = areaDAO.viewArea()

        length=len(areaVOList)
        print("__________________", areaVOList)

        return render_template('admin/viewArea.html', areaVOList=areaVOList,data=length)

    except Exception as ex:
        print(ex)


@app.route('/admin/deleteArea', methods=['GET'])
def adminDeleteArea():
    try:
        areaVO = AreaVO()

        areaDAO = AreaDAO()

        areaId = request.args.get('areaId')


        areaVO.areaId = areaId

        areaDAO.deleteArea(areaVO)

        return redirect(url_for('adminViewArea'))
    except Exception as ex:
        print(ex)


@app.route('/admin/editArea', methods=['GET'])
def adminEditArea():
    try:
        areaVO = AreaVO()

        areaDAO = AreaDAO()

        areaId = request.args.get('areaId')

        areaVO.areaId = areaId

        areaVOList = areaDAO.editArea(areaVO)

        print("=======areaVOList=======", areaVOList)


        print("=======type of areaVOList=======", type(areaVOList))

        return render_template('admin/editArea.html', areaVOList=areaVOList)
    except Exception as ex:
        print(ex)


@app.route('/admin/updateArea', methods=['POST'])
def adminUpdateArea():
    try:

        areaId = request.form['areaId']
        areaName = request.form['areaName']
        areaPincode = request.form['areaPincode']

        areaVO = AreaVO()
        areaDAO = AreaDAO()

        areaVO.areaId = areaId
        areaVO.areaName = areaName
        areaVO.areaPincode = areaPincode


        areaDAO.updateArea(areaVO)

        return redirect(url_for('adminViewArea'))
    except Exception as ex:
        print(ex)
