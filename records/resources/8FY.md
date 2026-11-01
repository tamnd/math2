---
records:
    - id: 8FYGQVTHRK
      kind: problem-set
      title: KöMaL Problems in Mathematics, December 2006
      creators:
        - name: KöMaL editorial board
          role: editor
      date: 2006-12
      msc:
        - code: 00A07
          from: komal
        - code: 97U40
          from: komal
      expressions:
        - key: e1
          kind: edition
          language: en
          date: 2006-12
          structure: 8FYGQVTHRK/e1.json
      relations:
        - kind: part_of
          to: 4T7QDPBW1N
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: komal
          snapshot: blake3:3658e660acc064da2c1a894c81d6f74fed1bee98fd8e0b9c468109c4c7e40452
          native_id: 2006-12
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
    - id: 8FYPNKPW5X
      kind: monograph
      title: 'Differential Geometrical Methods in Mathematical Physics: Proceedings of the Conferences Held at Aix-en-Provence, September 3 – 7, 1979 and Salamanca, September 10 – 14, 1979'
      creators:
        - name: P. L. García
          role: editor
        - name: A. Pérez-Rendón
          role: editor
        - name: J. M. Souriau
          role: editor
      date: "1980"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 53-06
          from: zbmath_search
        - code: 55Rxx
          from: zbmath_search
        - code: 57Rxx
          from: zbmath_search
        - code: 81-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1980"
          ids:
            doi: 10.1007/bfb0089722
            zbl: "0436.00018"
            zbl_id: "3679735"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1980"
              ids:
                isbn:
                    - "9783540102755"
                    - "9783540384052"
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
          native_id: 10.1007/bfb0089722
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3679735"
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
