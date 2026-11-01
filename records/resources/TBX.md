---
records:
    - id: TBXGWP0ET3
      kind: monograph
      title: Seminar über Potentialtheorie
      creators:
        - name: H. Bauer
          role: editor
      date: "1968"
      expressions:
        - key: e1
          kind: edition
          language: de
          date: "1968"
          ids:
            doi: 10.1007/bfb0080473
            zbl: "0174.16002"
            zbl_id: "3277889"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1968"
              ids:
                isbn:
                    - "9783540042396"
                    - "9783540358848"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0080473
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3277889"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: TBXXDQ00Q8
      kind: problem-set
      title: KöMaL Problems in Mathematics, May 2002
      creators:
        - name: KöMaL editorial board
          role: editor
      date: 2002-05
      msc:
        - code: 00A07
          from: komal
        - code: 97U40
          from: komal
      expressions:
        - key: e1
          kind: edition
          language: en
          date: 2002-05
          structure: TBXXDQ00Q8/e1.json
      relations:
        - kind: part_of
          to: 4T7QDPBW1N
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: komal
          snapshot: blake3:3658e660acc064da2c1a894c81d6f74fed1bee98fd8e0b9c468109c4c7e40452
          native_id: 2002-05
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
