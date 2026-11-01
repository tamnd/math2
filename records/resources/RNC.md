---
records:
    - id: RNCGFXSTDG
      kind: problem-set
      title: KöMaL Problems in Mathematics, October 2009
      creators:
        - name: KöMaL editorial board
          role: editor
      date: 2009-10
      msc:
        - code: 00A07
          from: komal
        - code: 97U40
          from: komal
      expressions:
        - key: e1
          kind: edition
          language: en
          date: 2009-10
          structure: RNCGFXSTDG/e1.json
      relations:
        - kind: part_of
          to: 4T7QDPBW1N
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: komal
          snapshot: blake3:3658e660acc064da2c1a894c81d6f74fed1bee98fd8e0b9c468109c4c7e40452
          native_id: 2009-10
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
    - id: RNCN60VTM7
      kind: monograph
      title: Simplicial Complexes of Graphs
      creators:
        - name: Jakob Jonsson
          role: author
      date: "2008"
      msc:
        - code: 05-01
          from: zbmath_search
        - code: 55U10
          from: zbmath_search
        - code: 06A11
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2008"
          ids:
            doi: 10.1007/978-3-540-75859-4
            zbl: "1152.05001"
            zbl_id: "5209738"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2008"
              ids:
                isbn:
                    - "9783540758587"
                    - "9783540758594"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-540-75859-4
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "5209738"
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
---
