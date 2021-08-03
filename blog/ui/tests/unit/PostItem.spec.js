import { mount } from "@vue/test-utils";

import PostItem from "@/components/PostItem.vue";

describe("PostItem", () => {
  test("If user clicks the post, should send browser to post URL", () => {
    const wrapper = mount(PostItem, {
      props: {
        item: {
          id: 11,
          title: "Hola desde vue",
          image: "http://127.0.0.1:8000/static/img/unity_mbGEGhn.png",
          content:
            "# Hola Vue\n\nHola desde vueHola desde vueHola desde vueHola desde vueHola desde vueHola desde vueHola desde vueHola desde vueHola desde vueHola desde vueHola desde vueHola desde vue",
          date: "2021-04-21T03:40:19.343761Z",
          description:
            "Hola desde vueHola desde vueHola desde vueHola desde vueHola desde vueHola desde vueHola desde vue",
          visible: true,
          user: { username: "marcos" },
        },
      },
    });

    const urlImage = wrapper
      .find('img[testid="imgPostItem"]')
      .attributes("src");
    expect(urlImage).toEqual(
      "http://127.0.0.1:8000/static/img/unity_mbGEGhn.png"
    );

    const title = wrapper.find('h3[testid="titlePostItem"]').text();
    expect(title).toEqual("Hola desde vue");

    const description = wrapper.find('p[testid="descriptionPostItem"]').text();
    expect(description).toEqual(
      "Hola desde vueHola desde vueHola desde vueHola desde vueHola desde vueHola desde vueHola desde vue"
    );

    const urlPost = wrapper.find('a[testid="linkPostItem"]').attributes("href");
    expect(urlPost).toEqual(`/post/11`);
  });
});
