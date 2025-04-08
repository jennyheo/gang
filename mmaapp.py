               st.markdown(':blue-background[**전문특기병**]')
               st.markdown('군악, 의장')
               st.markdown(':blue-background[**동반입대병**]')
               st.markdown('일반')            
               st.markdown(':blue-background[**직계가족복무부대병**]')
               st.markdown('일반')
          with st.expander('4️⃣ 공군병 모집'):
               st.markdown(':blue-background[**모집분야 및 복무기간**]')
               st.markdown('일반·전문기술병 등 3개분야 10개 직종 / 21개월 복무')
               st.divider()
               st.markdown(':blue-background[**일반·기술병**]')
               st.markdown('일반, 전자계산, 화생방, 의무, 기계, 차량운전, 차량정비, 통신전자전기')
               st.markdown(':blue-background[**전문특기병**]')
               st.markdown('군악, 의장')
          st.divider()
          st.write(f'✍️ 병역진로설계')
          st.markdown('- 입영 전 자신의 적성·전공 등을 고려하여 군 복무 및 전역 후 진로를 체계적으로 설계하도록 지원하는 프로그램입니다.')
          with st.expander('🤖 병역진로설계지원센터란'):
               st.markdown('병역을 이행할 사람에게 적성에 맞는 군특기 추천·상담, 군생활정보제공, 군체험·교육 프로그램 등을 상시 제공하는 복합공간')
               st.markdown(':blue-background[**직업선호도 검사**]')
               st.markdown('병무청 누리집에서 신청')
               st.markdown('📖:orange-background[병무청 누리집 ▸ 민원신청 ▸ 병역진로설계 ▸ 직업선호도검사]')
               st.markdown(':blue-background[**설명회**]')
               st.markdown('병역이행절차안내, 군생활 및 자기계발 정보제공')
               st.markdown(':blue-background[**병역진로상담**]')
               st.markdown('직업선호도검사결과 활용, 군특기 추천 등 병역진로설계')
               st.markdown(':blue-background[**군 적용 체험·교육**]')
               st.markdown('군 보급품 전시, 군 장비 모의체험  \n (체력검정, 전차SIM, 드론VR등)')
          with st.expander('💡 병역진로설계서비스 신청방법'):
               st.markdown('온라인 신청')
               st.link_button("병역진로설계 상담신청 안내➡️", "https://www.mma.go.kr/byjr/01/bYJRContents.do?mc=mma0002535")               
               st.markdown(':blue[_※ 병역판정검사를 받지 않은 사람도 온라인서비스 신청 가능_]')
          st.markdown("")
          st.markdown("")
          st.markdown(f"#### 🎯 현역(모집)병 안내 전체 내려받기")
          with open("downloadfile.pdf", "rb") as pdf_file:
               PDFbyte = pdf_file.read()
               st.download_button(label="⭐ 현역(모집)병 입영안내 다운로드(PDF)",
                    data=PDFbyte,
                    file_name="현역(모집)병입영안내.pdf",
                    mime='application/octet-stream')



     elif user_name == '사회복무요원소집대상' :
          st.markdown(f'✍️ 사회복무요원 소집 제도')
          st.markdown(f'- 공익을 목적으로 국가기관, 지방자치단체, 공공단체 및 사회복지시설에서 사회복지, 보건의료, 교육문화, 환경안전 등의 사회서비스 업무 및 행정업무 등을 지원하는 병역의무의 한 형태입니다.') 
          with st.expander('📢 대상'):
               st.markdown('병역판정검사 결과 보충역으로 병역처분된 사람')
          with st.expander('🏢 복무기관'):
               st.markdown('국가기관, 지방자치단체, 공공단체 및 사회복지시설')
          with st.expander('🎁 복무분야'):
               st.markdown('사회복지, 보건의료, 교육문화, 환경안전 등의 사회서비스 업무 및 행정업무 등의 지원업무')
          with st.expander('🗓️ 복무기간'):
               st.markdown('21개월')
          with st.expander('✍🏼 복무형태'):
               st.markdown('출·퇴근 근무하며 소속기관장의 지휘감독을 받음')
          with st.expander('💵 처우'):
               st.markdown('현역병 봉급 상당액의 보수 및 직무수행에 필요한 여비 등 지급')

          st.divider()
          st.markdown(f'✍️ 사회복무요원 소집일자 및 복무기관 결정')
          st.markdown(f'- 사회복무요원 소집 신청은 본인이 직접 신청하는 본인선택과 신청하지 않은 사람에 대해 주소지 관할 지방병무청장이 소집순서에 따라 일자와 기관을 결정하는 직권통지로 구분됩니다.') 
     
          with st.expander('🙋🏻‍♂️ 본인선택'):
               st.markdown(':blue-background[**신청시기 및 선발방법**]')
               st.markdown('다음연도 소집일자 및 복무기관 본인선택은 1차(11월 중)와 2차(12월 중)로 나누어 신청을 받으며, '+'**탈락횟수, 나이 등 선발기준에 의해 선발**')
               st.markdown(':blue-background[**신청방법**]')
               st.markdown('📖:orange-background[1차 : 병무청 누리집 ▸ 민원신청 ▸ 병무민원 ▸ 사회복무 ▸ 재학생 및 국외입영연기자 소집신청(선발)]')
               st.markdown('📖:orange-background[2차 : 병무청 누리집 ▸ 민원신청 ▸ 병무민원 ▸ 사회복무 ▸ 소집일자 및 복무기관 본인선택(선발)]')
               st.markdown(':blue[_※접수시기, 선발기준 등은 변동가능, 병무청 누리집 공지 참고_]')
          with st.expander('📌 지방병무청 직권통지'):
               st.markdown('본인선택하지 않은 별도·일반 소집대상으로 관할 지방병무청에서 연중 선발')

          st.divider()
          st.markdown(f'✍️ 사회복무요원 현역복무 희망 신청')
          st.markdown(f'- 사회복무요원(복무중인 경우 포함)이 현역 복무를 희망하는 경우 신청합니다.') 
     
          with st.expander('📒 신청대상'):
               st.write('사회복무요원 소집대상, 사회복무요원으로 복무 중인 사람')
               st.write('(단, 남은 복무기간이 현역의 복무기간으로 환산했을때 6개월 이상 남은 사람으로 한정함)')
               st.write(':blue[_※수형사유 보충역 및 현역부적합 심사에 따른 보충역은 비대상_]')
          with st.expander('🚩 처리절차'):
               st.write('신청서 제출 ▸ 대상여부 확인 ▸ 병역처분 변경 신청 ▸ (신체검사 없이) 현역병입영 대상자로 처분변경 후 현역병 입영신청 또는 모집병 지원')
               st.link_button("병역처분변경원 출원 안내➡️", "https://mma.go.kr/contents.do?mc=usr0000173")
               st.write(':blue[_※ 신청은 1회로 제한, 신청에 따라 현역병입영 대상자로 변경된 사람은 신청을 취소할 수 없음_]')


     elif user_name == '전시근로역' :
          st.write('병역판정검사 또는 신체검사 결과 현역 또는 보충역 복무는 할 수 없으나 전시근로소집에 의한 군사지원 업무는 감당할 수 있다고 결정된 사람')
          st.write('군복무 및 예비군도 면제되며, 민방위에 편성되어 관련 교육 등을 받게 됩니다. 추후 민방위 편성 및 교육관련 문의는 주소지 읍·면·동 주민자치센터로 문의하시면 됩니다.')
     elif user_name == '병역면제' :
          st.write('현역, 보충역, 예비군, 민방위, 전시근로역 등의 모든 병역의무가 완전히 면제되는 것으로 평시든 전시든 병역과 관련된 어떤 의무도 없습니다.')
     elif user_name == '재신체검사대상' :
          st.write('병역판정검사 시 신체등급 7급으로 질병치료 후 다시 검사를 받는 사람입니다.')
     else: 
          st.write('')
