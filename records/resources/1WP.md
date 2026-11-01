---
records:
    - id: 1WP6RR4BEQ
      kind: monograph
      title: 'Number Theory: Proceedings of the 4th Matscience Conference held at Ootacamund, India, January 5–10, 1984'
      creators:
        - name: Krishnaswami Alladi
          role: editor
      date: "1982"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 11-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1982"
          ids:
            doi:
                - 10.1007/bfb0075746
                - 10.1007/bfb0097171
            zbl: "0476.00003"
            zbl_id: "3746989"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1985"
              ids:
                isbn:
                    - "9783540152224"
                    - "9783540396420"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1982"
              ids:
                isbn:
                    - "9783540115687"
                    - "9783540392798"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0075746
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0097171
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3746989"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: 1WPPDSF0EJ
      kind: preprint
      title: Higher-Order Mean-Field Control Barrier Functions
      creators:
        - name: Levon Nurbekyan
          role: author
        - name: Samy Wu Fung
          role: author
      date: "2026-09-27"
      msc:
        - code: 49-XX
          from: arxiv
        - code: 90-XX
          from: arxiv
        - code: 93-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-09-27"
          ids:
            arxiv: "2609.33852"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.33852"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2609.33852"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
