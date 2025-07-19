import streamlit as st
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

def create_docx(paragraphs, filename):
    doc = Document()
    doc.add_heading('Petição', 0)

    for section in doc.sections:
        section.top_margin = Cm(3)
        section.bottom_margin = Cm(2)
        section.left_margin = Cm(3)
        section.right_margin = Cm(2)

    for para, style_choice in paragraphs:
        p = doc.add_paragraph(para)
        run = p.runs[0]
        if style_choice.lower() == 'corpo':
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
            p.paragraph_format.line_spacing = Pt(18)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.first_line_indent = Cm(1.25)
        elif style_choice.lower() == 'citação':
            run.font.name = 'Times New Roman'
            run.font.size = Pt(10)
            p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
            p.paragraph_format.left_indent = Cm(4)
            p.paragraph_format.line_spacing = Pt(12)
            p.paragraph_format.space_after = Pt(6)
        elif style_choice.lower() == 'título':
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p.paragraph_format.space_after = Pt(6)
        elif style_choice.lower() == 'endereçamento':
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
            p.paragraph_format.line_spacing = Pt(18)
            p.paragraph_format.space_after = Pt(6)
        elif style_choice.lower() == 'pedidos':
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
            p.paragraph_format.line_spacing = Pt(18)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.first_line_indent = Cm(1.25)

    doc.save(filename)

def main():
    st.set_page_config(page_title="Formatador ABNT", layout="wide")
    st.title("📄 Formatador de Peças Processuais - ABNT")
    st.header("by Cariolano")

    uploaded_file = st.file_uploader("📎 Selecione o arquivo .txt", type="txt")

    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        paragraphs = [para for para in text.split('\n') if para.strip()]

        st.subheader("📝 Aplique a formatação desejada para cada parágrafo")
        formatted_paragraphs = []

        for i, para in enumerate(paragraphs):
            st.markdown(f"**Parágrafo {i+1}:**")
            st.text_area(f"Texto:", value=para, height=100, key=f"text_{i}", disabled=True)
            style_choice = st.selectbox(
                "Escolha a formatação:",
                ["Corpo", "Citação", "Título", "Endereçamento", "Pedidos"],
                key=f"style_{i}"
            )
            formatted_paragraphs.append((para, style_choice))

        if st.button("👁️ Pré-visualizar Documento"):
            st.subheader("📄 Pré-visualização")
            for i, (para, style) in enumerate(formatted_paragraphs):
                st.markdown(f"**{style}**")
                st.write(para)
                st.markdown("---")

        if st.button("💾 Gerar e Baixar Documento"):
            output_filename = "peticao_trabalhista.docx"
            create_docx(formatted_paragraphs, output_filename)
            with open(output_filename, "rb") as file:
                st.download_button(
                    label="📥 Baixar Documento",
                    data=file,
                    file_name=output_filename,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

if __name__ == "__main__":
    main()
