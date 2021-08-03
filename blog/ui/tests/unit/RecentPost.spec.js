import { mount } from "@vue/test-utils";
import { getPosts } from "@/services/BackendServices.js";
import RecentPost from "@/components/RecentPosts.vue";
import flushPromises from "flush-promises";

jest.mock("@/services/BackendServices.js");

beforeEach(() => {
  jest.clearAllMocks();
});

describe("RecentPost", () => {
  test("Component should render the exact amount of post comming from API Response", async () => {
    const mockResponse = [
      {
        id: 12,
        title: "Prueba 2 desde vue Chido",
        image: "http://127.0.0.1:8000/static/img/vue_aaUsEz4.jpg",
        content:
          "<p>&lt;p&gt;&lt;p&gt;&lt;p&gt;&lt;p&gt;&lt;p&gt;&lt;p&gt;&lt;p&gt;&lt;p&gt;&lt;h1 id=&quot;prueba-2-vue&quot;&gt;Prueba 2 Vue&lt;/h1&gt;\n&lt;p&gt;Prueba 2 desde vue \nPrueba 2 desde vue\nPrueba 2 desde vue\nPrueba 2 desde vue\nPrueba 2 desde vue&lt;/p&gt;&lt;/p&gt;&lt;/p&gt;&lt;/p&gt;&lt;/p&gt;&lt;/p&gt;&lt;/p&gt;&lt;/p&gt;&lt;/p&gt;</p>",
        date: "2021-04-21T03:45:20.895537Z",
        description:
          "Prueba 2 desde vuePrueba 2 desde vuePrueba 2 desde vuePrueba 2 desde vuePrueba 2 desde vuePrueba 2 desde vuePrueba 2 desde vue",
        visible: true,
        user: { username: "marcos" },
      },
      {
        id: 10,
        title: "Virus",
        image: "http://127.0.0.1:8000/static/img/virus.jpg",
        content:
          '<h1>Virus</h1>\r\n\r\n<p><a href="https://es.wikipedia.org/wiki/Virus#mw-head">Ir a la navegaci&oacute;n</a><a href="https://es.wikipedia.org/wiki/Virus#searchInput">Ir a la b&uacute;squeda</a></p>\r\n\r\n<p>Para otros usos de este t&eacute;rmino, v&eacute;anse&nbsp;<a href="https://es.wikipedia.org/wiki/Virus_(desambiguaci%C3%B3n)" title="Virus (desambiguación)">Virus (desambiguaci&oacute;n)</a>&nbsp;y&nbsp;<a href="https://es.wikipedia.org/wiki/Viral_(desambiguaci%C3%B3n)" title="Viral (desambiguación)">Viral (desambiguaci&oacute;n)</a>.wiki/Microscopio_electr%C3%B3nico_',
        date: "2021-03-04T01:42:15.286909Z",
        description:
          "Este post es genial, dale click para que aprendas cosas interesantes y alimente tu curiosidad",
        visible: false,
        user: { username: "testuser_1" },
      },
      {
        id: 2,
        title: "Segundo Blog",
        image: "http://127.0.0.1:8000/static/img/prueba_ShFirVO.jpg",
        content:
          "<h1>Lorem Ipsum</h1>\r\n\r\n<h4><em>&quot;Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...&quot;</em></",
        date: "2021-02-26T02:44:54.644390Z",
        description:
          "Este post es genial, dale click para que aprendas cosas interesantes y alimente tu curiosidad",
        visible: false,
        user: { username: "marcos" },
      },
    ];

    getPosts.mockResolvedValueOnce(mockResponse);

    const wrapper = mount(RecentPost, {
      global: {
        stubs: {
          PostItem: {
            template: '<article testid="PostItemFake"></article',
          },
        },
      },
    });

    await flushPromises();
    expect(getPosts).toHaveBeenCalledTimes(1);

    const posts = wrapper.findAll('article[testid="PostItemFake"]');
    expect(posts).toHaveLength(3);
  });
});
