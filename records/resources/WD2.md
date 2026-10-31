---
records:
    - id: WD24AT6N8K
      kind: edited-volume
      title: Graph Colorings
      creators:
        - name: Marek Kubale
          role: editor
      date: "2004"
      msc:
        - code: 05C15
          from: zbmath_search
        - code: 05-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2004"
          ids:
            doi: 10.1090/conm/352
            zbl: "1064.05061"
            zbl_id: "2124062"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2004"
              ids:
                isbn:
                    - "9780821834589"
                    - "9780821856871"
                    - "9780821879429"
              access:
                class: record
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/352
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "2124062"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: WD2NCBV9F0
      kind: preprint
      title: Reliable Cellular Automata with Self-Organization
      creators:
        - name: Peter Gacs
          role: author
      date: "2000-03-20"
      msc:
        - code: 60-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.PR
        - system: arxiv
          code: cs.DC
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2000-03-20"
          ids:
            arxiv: math/0003117
            doi: 10.1023/a:1004823720305
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: math/0003117
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: math/0003117
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
---
