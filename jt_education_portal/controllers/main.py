# -*- coding: utf-8 -*-
##############################################################################
#
#    Jupical Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Jupical Technologies(<http://www.jupical.com>).
#    Author: Jupical Technologies Pvt. Ltd.(<http://www.jupical.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import fields, http, _
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request
from odoo.exceptions import AccessError, MissingError

class EducationPortal(CustomerPortal):

    # def sitemap_stud(env, rule, qs):
    #     if not qs or qs.lower() in '/my/issue_books_list':
    #         yield {'loc': '/my/issue_books_list'}

    #     student_data = request.env['res.partner']
    #     dom = sitemap_qs2dom(qs, '/my/issue_books_list/parent', student_data._rec_name)
    #     dom += env['website'].get_current_website().website_domain()
    #     for student in student_data.search(dom):
    #         loc = '/my/issue_books_list/parent/%s' % slug(student)
    #         if not qs or qs.lower() in loc:
    #             yield {'loc': loc}

    # @http.route([
    #     '''/my/issue_books_list''',
    #     '''/my/issue_books_list/page/<int:page>''',
    #     '''/my/issue_books_list/parent/<model('issue.books'):student_data>''',        
    # ], type='http', auth="public", website=True,sitemap = sitemap_stud)
    

    @http.route([
        '/my/issue_books_list'
        ], type='http', auth="user", website=True)
    def portal_my_issue_books_list(self, page=0, student_data = None,date_begin=None, date_end=None, sortby=None, **kw):

        values = {}
        stud_issue_list=[]
        issue_links =[]
        issue_result ={}

        partner = request.env.user.partner_id
        student_obj = request.env['res.partner']
        student = student_obj.sudo().search([('id','=',partner.id)], limit=1)
        # print("partner_id.........",student)
        issue_list_obj = request.env['issue.books']
        stud_issue_list = issue_list_obj.sudo().search([('student_id','=',student.id)])
        #print("issue list.........",stud_issue_list)

        #loop for Creating URL With ID. 
        for issue in stud_issue_list:
            issue_detail_url = '/my/issue_books/'+str(issue.id)
            issue_links.append(issue_detail_url) 
        
        #loop for combining two list in one dictionary and then send that combined dictionary to template where list is being displayed.    
        for link_info,issue_info in zip(issue_links,stud_issue_list):
            issue_result.update({link_info:issue_info})
        

        #print("issue Result..........",issue_result)
        values.update({
            'issue_books_list':issue_result,
            # 'issue_links':issue_links,
        })
        return request.render("jt_education_portal.portal_issue_books_list", values)

    @http.route(['/my/issue_books/<model("issue.books"):issue>'], type='http', auth="user", website=True)
    def portal_my_issue_books(self,issue, page=1, date_begin=None, date_end=None, sortby=None, **kw):

        values = {}
        issue_book_obj = request.env['issue.books']
        book_issues = issue_book_obj.sudo().search([('id', '=', issue.id)])
        #print ("ADSFASDF",book_issues)
        values.update({
            'issue_books': book_issues
        })

        # print ("values :::::",values)

        return request.render("jt_education_portal.portal_issue_books", values)

    @http.route(['/my/membership'], type='http', auth="user", website=True)
    def portal_my_membership(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):

        values = {}
        partner = request.env.user.partner_id
        student_obj = request.env['res.partner']
        student = student_obj.sudo().search([('id','=',partner.id)], limit=1)
        membership_obj = request.env['library.memberships']
        stud_membership = membership_obj.sudo().search([('student_id','=',student.id)])
        values.update({
            'membership':stud_membership
        })
        return request.render("jt_education_portal.portal_membership", values)

    @http.route(['/my/exam_list'], type='http', auth="user", website=True)
    def portal_my_exam_list(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = {}
        stud_exam_list=[]
        exam_links =[]
        exam_result ={}

        partner = request.env.user.partner_id
        student_obj = request.env['res.partner']
        student = student_obj.sudo().search([('id','=',partner.id)], limit=1)
        # print("partner_id.........",student)
        exam_list_obj = request.env['student.exam']
        stud_exam_list = exam_list_obj.sudo().search([('student_ids','=',student.id)])
        #print("exam list.........",stud_exam_list)

        #loop for Creating URL With ID. 
        for exam in stud_exam_list:
            exam_detail_url = '/my/exam/'+str(exam.id)
            exam_links.append(exam_detail_url) 
        
        #loop for combining two list in one dictionary and then send that combined dictionary to template where list is being displayed.    
        for link_info,exam_info in zip(exam_links,stud_exam_list):
            exam_result.update({link_info:exam_info})
        

        #print("Exam Result..........",exam_result)
        values.update({
            'exam_list':exam_result,
            # 'exam_links':exam_links,
        })
        return request.render("jt_education_portal.portal_exam_list", values)

    @http.route(['/my/exam/<model("student.exam"):exam>'], type='http', auth="user", website=True)
    def portal_my_exam(self, exam, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = {}
        # partner = request.env.user.partner_id
        # student_obj = request.env['res.partner']
        # student = student_obj.search([('id','=',partner.id)], limit=1)
        exam_obj = request.env['student.exam']
        stud_exam = exam_obj.sudo().search([('id','=',exam.id)])
        #print("..........................",exam_obj,stud_exam)
        values.update({
            'exam':stud_exam,
        })
        return request.render("jt_education_portal.portal_exam", values)

    @http.route(['/my/result_list'], type='http', auth="user", website=True)
    def portal_my_result_list(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):

        values = {}
        stud_result_list=[]
        result_links =[]
        exam_result ={}

        partner = request.env.user.partner_id
        student_obj = request.env['res.partner']
        student = student_obj.sudo().search([('id','=',partner.id)], limit=1)
        # print("partner_id.........",student)
        result_list_obj = request.env['student.result']
        stud_result_list = result_list_obj.sudo().search([('student_id','=',student.id)])
        # print("exam list.........",stud_result_list)

        #loop for Creating URL With ID. 
        for res in stud_result_list:
            exam_detail_url = '/my/result/'+str(res.id)
            result_links.append(exam_detail_url) 
        
        #loop for combining two list in one dictionary and then send that combined dictionary to template where list is being displayed.    
        for link_info,result_info in zip(result_links,stud_result_list):
            exam_result.update({link_info:result_info})
        

        # print("Exam Result..........",exam_result)
        values.update({
            'result_list':exam_result,
            # 'result_links':result_links,
        })
        return request.render("jt_education_portal.portal_result_list", values)

    @http.route(['/my/result/<model("student.result"):result>'], type='http', auth="user", website=True)
    def portal_my_result(self, result, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = {}
        result_obj = request.env['student.result']
        stud_result = result_obj.sudo().search([('id','=',result.id)])
        # print("..............................",stud_result)

        values.update({
            'result':stud_result,
        })
        return request.render("jt_education_portal.portal_result", values)
    
    @http.route(['/my/event'], type='http', auth="user", website=True)
    def portal_my_event(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):

        values = {}
        partner = request.env.user.partner_id
        student_obj = request.env['res.partner']
        student = student_obj.sudo().search([('id','=',partner.id)], limit=1)
        event_obj = request.env['event.registration']
        stud_event = event_obj.sudo().search([('partner_id','=',student.id)])
        values.update({
            'event':stud_event
        })
        return request.render("jt_education_portal.portal_event", values)

    @http.route(['/my/fees_list'], type='http', auth="user", website=True)
    def portal_my_fees_list(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):

        values = {}
        stud_fees_list=[]
        fees_links =[]
        fees_result ={}

        partner = request.env.user.partner_id
        student_obj = request.env['res.partner']
        student = student_obj.sudo().search([('id','=',partner.id)], limit=1)
        fees_list_obj = request.env['fees.fees']
        stud_fees_list = fees_list_obj.sudo().search([('student','=',student.id)])

        #loop for Creating URL With ID. 
        for fees in stud_fees_list:
            fees_detail_url = '/my/fees/'+str(fees.id)
            fees_links.append(fees_detail_url) 
        
        #loop for combining two list in one dictionary and then send that combined dictionary to template where list is being displayed.    
        for link_info,fees_info in zip(fees_links,stud_fees_list):
            fees_result.update({link_info:fees_info})
        
        values.update({
            'fees_list':fees_result,
        })
        return request.render("jt_education_portal.portal_fees_list", values)

    @http.route(['/my/fees/<model("fees.fees"):fees>'], type='http', auth="user", website=True)
    def portal_my_fees(self,fees, page=1, date_begin=None, date_end=None, sortby=None, **kw):

        values = {}
        fees_obj = request.env['fees.fees']
        stud_fees = fees_obj.sudo().search([('id','=',fees.id)])
        values.update({
            'fees':stud_fees
        })
        return request.render("jt_education_portal.portal_fees", values)

    @http.route(['/my/assignment_list'], type='http', auth="user", website=True)
    def portal_my_assignment_list(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):

        values = {}
        stud_assignment_list=[]
        assignment_links =[]
        assignment_result ={}

        partner = request.env.user.partner_id
        student_obj = request.env['res.partner']
        student = student_obj.sudo().search([('id','=',partner.id)], limit=1)
        # print("partner_id.........",student)
        assignment_list_obj = request.env['student.assignment']
        stud_assignment_list = assignment_list_obj.sudo().search([('allocation_ids','=',student.id)])
        # print("assignment list.........",stud_assignment_list)

        #loop for Creating URL With ID. 
        for assignment in stud_assignment_list:
            assignment_detail_url = '/my/assignment/'+str(assignment.id)
            assignment_links.append(assignment_detail_url) 
        
        #loop for combining two list in one dictionary and then send that combined dictionary to template where list is being displayed.    
        for link_info,assignment_info in zip(assignment_links,stud_assignment_list):
            assignment_result.update({link_info:assignment_info})
        

        # print("Assignment Result..........",assignment_result)
        values.update({
            'assignment_list':assignment_result,
        })
        return request.render("jt_education_portal.portal_assignment_list", values)

    @http.route(['/my/assignment/<model("student.assignment"):assignment>'], type='http', auth="user", website=True)
    def portal_my_assignment(self, assignment, page=1, date_begin=None, date_end=None, sortby=None, **kw):

        values = {}
        assignment_obj = request.env['student.assignment']
        stud_assignment = assignment_obj.sudo().search([('id','=',assignment.id)])
        # print("..........................",assignment_obj,stud_assignment)
        values.update({
            'assignment':stud_assignment,
        })
        return request.render("jt_education_portal.portal_assignment", values)

    @http.route(['/my/submission'], type='http', auth="user", website=True)
    def portal_my_submission(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):

        values = {}
        partner = request.env.user.partner_id
        student_obj = request.env['res.partner']
        student = student_obj.sudo().search([('id','=',partner.id)], limit=1)
        submission_obj = request.env['student.assignment.submission']
        stud_submission = submission_obj.sudo().search([('student_id','=',student.id)])
        values.update({
            'submission':stud_submission
        })
        return request.render("jt_education_portal.portal_submission", values)

    

    @http.route(['/my/exam/page/<model("student.exam"):student_exam>'], type='http', auth="user", website=True)
    def portal_my_exam_page(self,student_exam, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = {}
        exam_obj = request.env['student.exam']
        stud_exam = exam_obj.sudo().search([('id','=',student_exam.id)])
        #print("..........................",exam_obj,stud_exam)
        values.update({
            'exam':stud_exam,
        })
        return request.render("jt_education_portal.portal_exam", values)

    @http.route(['/my/result/page/<model("student.result"):student_result>'], type='http', auth="user", website=True)
    def portal_my_result_page(self,student_result, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = {}
        result_obj = request.env['student.result']
        stud_result = result_obj.sudo().search([('id','=',student_result.id)])
        #print("..........................",result_obj,stud_result)
        values.update({
            'result':stud_result,
        })
        return request.render("jt_education_portal.portal_result", values)


    @http.route(['/my/timetable_list'], type='http', auth="user", website=True)
    def portal_my_timetable_list(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = {}
        stud_timetable_list = []
        timetable_links = []
        day_timetable = {}

        partner = request.env.user.partner_id
        student_obj = request.env['res.partner']
        student = student_obj.sudo().search([('id','=',partner.id)], limit=1)
        timetable_list_obj = request.env['student.timetable']
        stud_timetable_list = timetable_list_obj.sudo().search([('student_ids','=',student.id)])
        
        #loop for Creating URL With ID. 
        for res in stud_timetable_list:            
            if res.timetable_mon:
                day_timetable_url = '/my/timetable_list/days/'+str(res.id)+"?week_day=0"
                timetable_links.append({'week_day':'Monday','url':day_timetable_url})
            if res.timetable_tue:
                day_timetable_url = '/my/timetable_list/days/'+str(res.id)+"?week_day=1"
                timetable_links.append({'week_day':'Tuesday','url':day_timetable_url})
            if res.timetable_wed:
                day_timetable_url = '/my/timetable_list/days/'+str(res.id)+"?week_day=2"
                timetable_links.append({'week_day':'Wednesday','url':day_timetable_url})
            if res.timetable_thur:
                day_timetable_url = '/my/timetable_list/days/'+str(res.id)+"?week_day=3"
                timetable_links.append({'week_day':'Thursday','url':day_timetable_url})
            if res.timetable_fri:
                day_timetable_url = '/my/timetable_list/days/'+str(res.id)+"?week_day=4"
                timetable_links.append({'week_day':'Friday','url':day_timetable_url})
            if res.timetable_sat:
                day_timetable_url = '/my/timetable_list/days/'+str(res.id)+"?week_day=5"
                timetable_links.append({'week_day':'Saturday','url':day_timetable_url})
            if res.timetable_sun:
                day_timetable_url = '/my/timetable_list/days/'+str(res.id)+"?week_day=6"
                timetable_links.append({'week_day':'Saunday','url':day_timetable_url})
    
        values.update({
            'timetable_list':timetable_links,         
        })
        return request.render("jt_education_portal.portal_timetable_list", values)

    @http.route(['/my/timetable_list/days/<model("student.timetable"):student_timetable>'], type='http', auth="user", website=True)
    def portal_my_timetable(self, student_timetable, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = {}
        day_obj = request.env['student.timetable.line']     
        stud_timetable = day_obj.sudo().search([('timetable_id','=',student_timetable.id),('week_day','=',kw["week_day"])])
        
        values.update({
            'timetable':stud_timetable,
        })
        return request.render("jt_education_portal.portal_timetable", values)


    @http.route(['/my/student_list'], type='http', auth="user", website=True)
    def portal_my_student_list(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):

        values = {}
        student_links =[]
        student_result ={}

        contact_obj = request.env['res.partner']

        parent_id = request.env.user.partner_id.id
        students = contact_obj.sudo().search([('parentsid','=',parent_id)])

        #loop for Creating URL With ID. 
        for stud in students:
            student_detail_url = '/my/student_1111/timetable/'+str(stud.id)
            student_links.append(student_detail_url) 


        print("Student--link---->>>>>>>>",student_links)
        
        #loop for combining two list in one dictionary and then send that combined dictionary to template where list is being displayed.    
        for link_info,student_info in zip(student_links,students):
            student_result.update({link_info:student_info})

        print("Student Result..........",student_result)
        values.update({
            'student_list':student_result,
        })
        return request.render("jt_education_portal.portal_student_list", values)

    @http.route(['/my/student_1111/timetable/<int:student_data>'], type='http', auth="user", website=True) 
    # @http.route(['/my/student_1111/timetable/<model("res.partner"):student_timetable>'], type='http', auth="user", website=True)
    def portal_my_student_detail_list(self, student_data,page=1, date_begin=None, date_end=None, sortby=None, **kw):
        print("student-daata------------------->",student_data)
        values = {}
        student_exam_links =[]
        student_exam_result ={}
        student_result_links =[]
        student_result_result ={}
        print("<<<<<<<<<<<<<<<<<-----------Bhumika Siddhapura------------------>>>>>>>>>>>")

        exam_obj = request.env['student.timetable'].sudo().search([])
        print("exam_obj=================",exam_obj)
        result_obj = request.env['student.result'].sudo().search([])
        #loop for Creating URL With ID. 
        for ex in exam_obj.student_ids:
            # print("ex.student_ids=======================",ex.student_id.ids)
            for rec in ex.student_ids.ids:
                print("ex==========================",ex)
                print("stud=========================",stud)
                if ex == stud:
                    student_exam_detail_url = '/my/exam/page/'+str(stud)
                    student_exam_links.append(student_exam_detail_url)

        for stud in result_obj:
          for rec in stud.student_id:
              print("rec.student_id==========",rec)
              if rec.id == stud:
                  student_result_detail_url = '/my/result/page/'+str(stud.id)
                  student_result_links.append(student_result_detail_url)


        print("Student Result Link--------->>",student_result_links)
        #loop for combining two list in one dictionary and then send that combined dictionary to template where list is being displayed.    
        for link_exam_info,student_exam_info in zip(student_exam_links,exam_obj):
            student_exam_result.update({link_exam_info:student_exam_info})

        for link_result_info,student_result_info in zip(student_result_links,result_obj):
          student_result_result.update({link_result_info:student_result_info})
        
        values.update({
            'student_list_exam':student_result_links,
            'student_list_result':student_result_result
        })
        return request.render("jt_education_portal.portal_student_details_list", values)


